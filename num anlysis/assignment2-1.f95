program newton
	implicit none
    integer:: i
    real::x, tol, xb, y, yd
    read *,x
    
    tol=0.001
    xb=x
    i=0
20  i=i+1
    y=xb**2-sin(xb)	
    yd=2*xb-cos(xb)	
    x=xb-y/yd

    if (abs(x-xb)>=tol) then
      xb=x
      print *,x
      goto 20
    end if

    print 30,'final value is=',x
30  format (A,f8.5)
    
    
   
end program newton