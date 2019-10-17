clear all
close all

M = csvread('capital_federal.csv');

Xmin = 0;
Ymin = 0;
Xmax = 17975.40258 ;
Ymax = 19863.14275;
sqr = [Xmin Ymin; Xmin Ymax; Xmax Ymax; Xmax Ymin; Xmin Ymin];

figure
%plot(c(:,1),c(:,2),sqr(:,1),sqr(:,2))
plot(M(:,1),M(:,2),sqr(:,1),sqr(:,2))

% 0 0 9854.149231 9900.419522  --> Python