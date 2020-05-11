# spike-farm

Focus on numpy and pandas to process large climate datasets to identify when spikes in tmax, tmin and precip have occurred. Focus on matplotlib and Seaborn to visualize results. Temperature spikes to be identified by determining WHEN, for example, the top decile of tmaxs occur. 

Basically, the procedure is to develop estimates, through bootstrapping, of the 10th and 90th percentile boundaries, then use these estimates to filter all of the data in the sampled population.

# To do:

1) Create a prototype ("mock-up") that runs on simulated temperature data using the linear equation below, 
  where x is the day and y is the simulated weather parameter: 

           a*cos(x) + b*sin(x) + random(e) = y

2) Download low-res daily PRISM data for Glacier Bay.








