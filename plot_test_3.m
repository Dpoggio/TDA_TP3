clear all
close all

M = [1 4 ; 2 5 ; 3 6 ; 6 6 ; 4 5 ; 5 3; 4 2 ; 2 1];
X = [M(:,1) ; M(1,1)];
Y = [M(:,2) ; M(1,2)];


figure
subplot(2,3,1); 
plot(X,Y, 'r.-', 'LineWidth',2, 'MarkerSize',20)

ini = 1; fin = 8;

subplot(2,3,2); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
mid = floor((ini + fin - 1)/2) + 1;
ini = mid;
% plot(X(4:7),Y(4:7), 'r.-', 'LineWidth',2, 'MarkerSize',20)
plot(X(ini:fin),Y(ini:fin), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,3); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
mid = floor((ini + fin - 1)/2) + 1;
fin = mid;
plot(X(ini:fin),Y(ini:fin), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,4); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
mid = floor((ini + fin - 1)/2) + 1;
fin = mid;
plot(X(ini:fin),Y(ini:fin), 'r.-', 'LineWidth',2, 'MarkerSize',20)

subplot(2,3,5); 
hold on
plot(X,Y, 'k.-', 'LineWidth',1, 'MarkerSize',20)
mid = floor((ini + fin - 1)/2) + 1;
fin = mid;
plot(X(fin),Y(fin), 'r.-', 'LineWidth',2, 'MarkerSize',20)

