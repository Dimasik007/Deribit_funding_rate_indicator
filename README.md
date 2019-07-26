# Deribit Funding Rate Indicator

Indicator that shows current 8h funding rate and average 4h funding rate on Deribit exchange in real time for BTC. 

### Getting Started

1) You should have Python 3.7 installed. --> https://www.python.org/downloads/

    a) for Windows: in the downloads dropdown menu select Windows, choose Latest Python 3 version, and choose Windows x86-64 executable installer
    
    b) during installation select "Add Python 3.7 to Path" option

2) Clone or download the project and go to the project directory. Open shell/terminal within Deribit_funding_rate_indicator directory

3) Install requirements for the project from requirements.txt file using:

    a) Windows: `pip install -r requirements.txt`

    b) Mac/Linux: `pip3 install -r requirements.txt`
 
4) Run plot_now.py file with python3.7

From the shell/terminal:

   a) Windows: `python plot_now.py`

   b) Mac/Linux: `python3 plot_now.py`

5) In the terminal/shell in the Deribit_funding_rate_indicator directory run 

`bokeh serve --show plot_now.py`

6) After that, a new window in your default browser will pop up and you will see the running indicator.

On hoovering your cursor below the right side of the graph, you will see a menu to the control the chart.

7) To stop indicator, close the browser window or shut down terminal/shell window


#### Prerequisites / Built With

Python 3.7

Bokeh 1.3.0 - interactive visualization library

To install: 
`pip install bokeh`

Pandas 0.25.0 - library providing high-performance data structures and data analysis tools for Python

To install: 
`pip install pandas`

#### Author

Dmytro Vnukov

#### License

This project is licensed under the MIT License - see the LICENSE.md file for details
