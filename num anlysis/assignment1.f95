Program assignment1
	Implicit none
    Integer :: i
    Real :: x,f,pi
    pi=3.141592
    
	open(unit=20,file="output.csv",status="unknown")
    do i=1,999
      x=2*pi*i/1000
      f=sin(x)-cos(x/4)+x
      
      write (20,*) x,f
    end do

    
   

End Program assignment1