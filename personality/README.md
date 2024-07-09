# Process Documentation

## 1. Power Query Editing of the `resultados` Table

### Step-by-Step Guide

1. **Load the Data**:
    ```m
    let
        // Load the data
        Source = Excel.CurrentWorkbook(){[Name="resultados"]}[Content],
        
        // Change the percentage columns to number type
        ChangedType = Table.TransformColumnTypes(Source,{{"paciente", type number}, {"comum", type number}, {"suspeita", type number}, {"confirmado", type number}}),
        
        // Calculate the mean and standard deviation for the comum column
        MeanComum = List.Average(ChangedType[comum]),
        StdDevComum = List.StandardDeviation(ChangedType[comum]),
        
        // Normalize the scores of other groups against the comum column
        AddNormalizedComum = Table.AddColumn(ChangedType, "NormalizedComum", each ([comum] - MeanComum) / StdDevComum),
        AddNormalizedPaciente = Table.AddColumn(AddNormalizedComum, "NormalizedPaciente", each ([paciente] - MeanComum) / StdDevComum),
        AddNormalizedSuspeita = Table.AddColumn(AddNormalizedPaciente, "NormalizedSuspeita", each ([suspeita] - MeanComum) / StdDevComum),
        AddNormalizedConfirmado = Table.AddColumn(AddNormalizedSuspeita, "NormalizedConfirmado", each ([confirmado] - MeanComum) / StdDevComum),
        
        // Select relevant columns
        SelectColumns = Table.SelectColumns(AddNormalizedConfirmado,{"paciente", "comum", "suspeita", "confirmado", "NormalizedComum", "NormalizedPaciente", "NormalizedSuspeita", "NormalizedConfirmado"})
    in
        SelectColumns
    ```

2. **Implement the M Code**:
    - Open Excel and load your data into a table named `resultados`.
    - Go to the `Data` tab and select `Get Data` > `From Other Sources` > `Blank Query`.
    - In the Power Query Editor, click on `Advanced Editor`.
    - Remove any existing code in the editor and paste the M code provided above.
    - Click `Done` to run the code.
    - Your normalized table will be created in Power Query. Click `Close & Load` to load it back into Excel.

## 2. VBA Code for Generating and Plotting Bell Curves

### VBA Code for Plotting Bell Curves for Columns A and B

```vba
Sub ScatterBellCurve()
    Dim ws As Worksheet
    Dim rngA As Range, rngB As Range
    Dim meanA As Double, meanB As Double
    Dim stdDevA As Double, stdDevB As Double
    Dim numPoints As Integer
    Dim i As Integer
    Dim z0 As Double, z1 As Double
    Dim u1 As Double, u2 As Double
    Dim xA As Double, yA As Double
    Dim xB As Double, yB As Double
    Dim chartObj As ChartObject
    Dim seriesA As Series, seriesB As Series
    
    Set ws = ThisWorkbook.Sheets("normalização")
    Set rngA = ws.Range("A9:A1008") ' Adjust the range to the actual number of samples you have
    Set rngB = ws.Range("B9:B1008") ' Adjust the range to the actual number of samples you have

    ' Calculate mean and standard deviation of the values in column A
    meanA = Application.WorksheetFunction.Average(rngA)
    stdDevA = Application.WorksheetFunction.StDev(rngA)
    
    ' Calculate mean and standard deviation of the values in column B
    meanB = Application.WorksheetFunction.Average(rngB)
    stdDevB = Application.WorksheetFunction.StDev(rngB)
    
    ' Number of points to generate for the bell curve
    numPoints = 100
    
    ' Clear existing data if any
    ws.Range("E9:H" & 8 + numPoints).Clear
    
    ' Generate data for the bell curve using the Box-Muller transform
    For i = 0 To numPoints - 1
        u1 = Rnd
        u2 = Rnd
        z0 = Sqr(-2 * Log(u1)) * Cos(2 * WorksheetFunction.Pi() * u2)
        z1 = Sqr(-2 * Log(u1)) * Sin(2 * WorksheetFunction.Pi() * u2)
        
        ' Data for column A
        xA = meanA + stdDevA * z0
        yA = (1 / (stdDevA * Sqr(2 * WorksheetFunction.Pi()))) * Exp(-0.5 * ((xA - meanA) / stdDevA) ^ 2)
        ws.Cells(9 + i, 5).Value = xA
        ws.Cells(9 + i, 6).Value = yA
        
        ' Data for column B
        xB = meanB + stdDevB * z0
        yB = (1 / (stdDevB * Sqr(2 * WorksheetFunction.Pi()))) * Exp(-0.5 * ((xB - meanB) / stdDevB) ^ 2)
        ws.Cells(9 + i, 7).Value = xB
        ws.Cells(9 + i, 8).Value = yB
    Next i
    
    ' Check if the chart already exists
    On Error Resume Next
    Set chartObj = ws.ChartObjects("BellCurveChart")
    On Error GoTo 0
    
    If chartObj Is Nothing Then
        ' Create new scatter plot
        Set chartObj = ws.ChartObjects.Add(Left:=400, Width:=600, Top:=50, Height:=400)
        chartObj.Name = "BellCurveChart"
        With chartObj.Chart
            .ChartType = xlXYScatterSmooth
            .HasTitle = True
            .ChartTitle.Text = "Bell Curve"
            .Axes(xlCategory, xlPrimary).HasTitle = True
            .Axes(xlCategory, xlPrimary).AxisTitle.Text = "Values"
            .Axes(xlValue, xlPrimary).HasTitle = True
            .Axes(xlValue, xlPrimary).AxisTitle.Text = "Probability Density"
        End With
    End If
    
    ' Add series for column A
    With chartObj.Chart
        Set seriesA = .SeriesCollection.NewSeries
        seriesA.Name = "Column A"
        seriesA.XValues = ws.Range("E9:E" & 8 + numPoints)
        seriesA.Values = ws.Range("F9:F" & 8 + numPoints)
        
        ' Add series for column B
        Set seriesB = .SeriesCollection.NewSeries
        seriesB.Name = "Column B"
        seriesB.XValues = ws.Range("G9:G" & 8 + numPoints)
        seriesB.Values = ws.Range("H9:H" & 8 + numPoints)
    End With
End Sub
```

### Instructions for Implementing VBA Code:

1. **Open Excel** and navigate to the worksheet named `normalização`.

2. **Insert a New Module**:
    - Press `Alt + F11` to open the VBA editor.
    - Insert a new module by right-clicking on any existing module or the `VBAProject` and selecting `Insert` > `Module`.

3. **Paste the VBA Code**:
    - Copy the provided VBA code and paste it into the new module.

4. **Run the Macro**:
    - Close the VBA editor.
    - Press `Alt + F8`, select `ScatterBellCurve`, and click `Run`.

5. **Review the Generated Data and Chart**:
    - The code will generate bell curve data in columns `E`, `F`, `G`, and `H`.
    - It will then create a scatter plot titled "Bell Curve" with the generated data for columns `A` and `B`.

This documentation ensures that you can successfully normalize data using Power Query and visualize bell curves with VBA in Excel.
