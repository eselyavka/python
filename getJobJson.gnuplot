set datafile separator ","
set terminal png size 1200,800
set output "getJobJson.png"
set title "JT submmited tasks for user"
set ylabel "Submitted tasks"
set yrange [*:10]
set xlabel "Date"
set xdata time
set timefmt "%s"
set format x "%H:%M:%S"
set xrange ["1432512000":"1432598400"]
set key left top
set grid
plot "jobReport.txt" using 1:2 with lines lw 2 lt 3 title 'User_tasks'
