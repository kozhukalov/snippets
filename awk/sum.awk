BEGIN {print "Calculating sum ..."}
{SUM += $1}
END {print "Result: "SUM}
