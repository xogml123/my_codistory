program trapazoidal
	implicit none
    real:: h,x(0:100),func(0:100),s,r,A,B
    integer:: N,i,w
3   print *,"How many Sections do you want to calculate with?"
	read *, N
    open(unit=30, file='assignment2.txt',status='unknown')
	do i=0,N!hdifference then multiplying
      read (30,*) x(i),func(i)
    end do
    
    
    A=x(0)
    B=x(N) !hdifference then multiplying
    h=(B-A)/N
    

    s=0
    do i=0,N
      
      w=2
      if (i==0 .or. i==N)then
        w=1
      end if
      s=s+w*func(i) !hdifference then multiplying
      
    end do

      s=s*h/2
      print *, 'Result is ',s

    
end program trapazoidal