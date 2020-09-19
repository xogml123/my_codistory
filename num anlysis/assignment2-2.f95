program newton
	implicit none
    integer:: i
    real::x, tol, xb, y, yd,pi,e
    read *,x
   
    e=2.71828
    pi=3.141592
    
    tol=0.001
    xb=x
    i=0
20  i=i+1
    y=2*e**xb-cos(pi*xb/3)	
    yd=2*e**xb+(pi/3)*sin(pi*xb/3)
    
    x=xb-y/yd

    if (abs(x-xb)>=tol) then
      xb=x
      print *,x
      goto 20
    end if

    print 30,'final value is=',x
30  format (A,f8.5)
    
    
   
end program newton