# SIMPLE PLOTTER
## FEATURE
* Two trace drawing
* Draw difference between traces
* File based data input
* Customization plot by input file

### INPUT FILE FORMAT
    ############################################################################################################################################
    # This is a comment
    # File must start with description string
    # Arguments separate by '/'
    # X-Axis Name / Y-Axis name at top plot / Y-Axis name at bottom plot / First trace name / Second trace name / legend position / legend size
    # top plot - two traces given in file
    # bottom plot (first trace - second trace)
    # legend possition posible value
    #       best, upper right, upper left, lower left, lower right,  right,  center left,  center right,  lower center,  upper center,  center
    # legend size possible value 
    #       xx-small, x-small, small, medium, large, x-large, xx-large, larger, smaller, None
    ############################################################################################################################################
    Frequency(GHz) / Insertion losses(dB) / Difference(dB) / Simulated / Measured / best / x-large
    11.2	-68.3	-52.8
    11.3	-62.4	-52
    11.4	-56.03	-45.8
    11.5	-49.05	-36
    11.6	-41.3	-30.2
    11.7	-32.5	-19.5
    11.8	-22.16	-6.8
    11.9	-9.29	-2.1
    12.0	-0.24	-1.24
    12.1	-0.15	-1.01
    12.2	-0.07	-0.86
    12.3	-0.07	-0.86
    12.4	-0.05	-0.7
    12.5	-0.06	-0.97
    12.6	-0.06	-0.86
