clear all
close all

M = csvread('capital_federal.csv');

% Xmin = -9016.359751;
% Ymin = -9904.671966;
% Xmax = 8959.042825 ;
% Ymax = 9958.470781;

Xmin = min(M(:,1));
Xmax = max(M(:,1));
Ymin = min(M(:,2));
Ymax = max(M(:,2));

sqr = [Xmin Ymin; Xmin Ymax; Xmax Ymax; Xmax Ymin; Xmin Ymin];


% (min(M(:,2)) + max(M(:,2))) / 2
figure
%plot(c(:,1),c(:,2),sqr(:,1),sqr(:,2))
plot(M(:,1),M(:,2),sqr(:,1),sqr(:,2))
%  plot(M(:,1) -5643800,M(:,2) -6169100)
% plot(M(:,1),M(:,2))
 
% 0 0 9854.149231 9900.419522  --> Python