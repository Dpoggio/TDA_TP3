clear all
close all

M = [1 4 ; 2 5 ; 3 6 ; 4 5 ; 5 3; 4 2 ; 2 1];
X = [M(:,1) ; M(1,1)];
Y = [M(:,2) ; M(1,2)];


figure
subplot(2,3,1); 
plot(X,Y, 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,2); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
plot(X(4:7),Y(4:7), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,3); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
plot(X(4:6),Y(4:6), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,4); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
plot(X(4:5),Y(4:5), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,5); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
plot(X(5),Y(5), 'r.-', 'LineWidth',2, 'MarkerSize',20)

