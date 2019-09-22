# Tesla Superchargers in France
Visualizing current Tesla Superchargers available in France using Python, Pandas and Folium.

## 1. Installing dependencies

Installing dependencies is the first thing you want to do.
```
pip install folium
pip install pandas
```

## 2. Understanding files in the directory

### Data
The data is in .csv and .xlsx format. As discussed in the article, use xlsx for this one. 
```
tesla-supercharger-france.csv
tesla-supercharger-france.xlsx
```

### Step by Step Solution
I have created different files for each step in creating the interactive dictionary, here's the description of what each file does. 

``` 
tesla1.py
```
> Import library and create base map.

```
tesla2.py
```
> Add a marker to a particular location.

```
tesla3.py
```
> Add multiple markers.

```
tesla4.py
```
> Use data to plot more than one markers.

```
tesla5.py
```
> Use custom icons

```
tesla6.py
```
> Cluster all the markers


Note: All files are executable and integrated with comments to help you understand each and every line/command of the code.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details
