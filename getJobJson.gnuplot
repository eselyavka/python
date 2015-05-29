if (!exists("username")) {
    username=system("echo $USER");
}

if (!exists("inputfile")) {
    inputfile='jobReportHourlyAgg.dat'
}

outPut = "MapReduceSlotUtilization".username."_".inputfile."Stat.png"
set datafile separator ","
set terminal png size 1200,800
set output outPut
set title "Map/Reduce slot utilization for user ".username
set ylabel "Slot count"
set yrange [0:100000]
set xlabel "Time"
set timefmt "%Y-%m-%d %H:%M:%S"
set xdata time
set format x "%Y-%m-%d %H:%M"
set xrange ["2015-05-27 06:00":"2015-05-28 07:00"]
set xtics "2015-05-27 06:00", 3600, "2015-05-28 07:00"
set auto x
set xtics rotate
set key left top
set grid
set style fill solid border -1
set boxwidth 0.5 relative
set style data histograms
set style histogram rowstacked
plot inputfile using 1:2 with boxes lc rgb "red" ti "map", \
     "" using 1:3 with boxes lc rgb "yellow" ti "reduce"
