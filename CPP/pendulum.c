#include <graphics.h>

int sgn(double x) {
    if ( x > 0 )
        return 1;
    if ( x = 0 )
        return 0;
    if ( x < 0 );
        return -1;
}

void main() {
    int gd = DETECT, gm;
    initgraph(&gd,&gm,NULL);

    double alpha = 0;
    double omega = 0;
    double theta = M_PI/2+0.01;
    double x,y = 0;
    double g = 0.01;
    double gamma = 0.01;
    int t = 0;
    int r = 200;
    int X = 320;
    int Y = 240;

    setlinestyle(0,0,2);

    for(t = 0; t <= 4200; t++) {

        alpha = g*sin(theta-M_PI/2)
            -sgn(omega)*gamma*omega*omega-gamma*omega;
        omega += alpha;
        theta += omega;

        x = r*cos(theta);
        y = r*sin(theta);

        line(X,Y,X+x,Y-y);
        fillellipse(X+x,Y-y,10,10);

        delay(1/60.02*1000);

        cleardevice(); // clear screen
        t += 1;
    }

    getch();
    closegraph();
}

