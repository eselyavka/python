set datafile separator ","
set terminal png size 1200,800
set output "MapReduceUserStat.png"
set title "JT submmited tasks for user"
set ylabel "Submitted tasks"
set yrange [0:2000]
set xlabel "Date"
set timefmt "%s"
set xdata time
set format x "%H:%M:%S"
set auto x
set key left top
set grid
plot "jobReport.dat" u 1:2 w lines lw 2 lt 3 ti 'map_tasks', '' u 1:3 w lines lw 2 lt 4 ti 'reduce_tasks'
