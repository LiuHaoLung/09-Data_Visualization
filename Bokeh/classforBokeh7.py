from bokeh.plotting import figure,output_file,show

# 設定資料，也可以是匯入資料
x = [10,20,30,40,50,60,70,80,90]
y = [11,12,13,14,15,16,17,18,19]

# 將檔案存為html，然後()裡面的就是html的檔名
output_file('line.html')

# 設定圖表變數p，且圖表表名(title)為Basic Line Plot，x軸是x_axis，y軸是y_axis
p = figure(title = 'Basic Line Plot',x_axis_label = 'x_axis',y_axis_label = 'y_axis')

# 顯示出來的線名(legend)為Price，線(width)的寬度為3
p.line(x,y,legend = 'Price',line_width = 3)

show(p)