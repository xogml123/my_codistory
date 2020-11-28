program simpson	
	implicit none
    real:: h,x(0:100),func(0:100),s,r,A,B,ss
    integer:: N,i,w,LS
    open(unit=30, file='assignment2.txt', status='unknown')
    
3   print *,"How many Sections do you want to calculate with?"
	read *, N
    
    ss=0    
    s=0      
    LS=0     
    
	if (N<3) then
      print *,"IMPOSSIBLE!!"
      go to 3
    end if
    do i=0,2*N !h-0.2
      read (30,*) x(i),func(i)
    end do
    
    
    A=x(0)
    B=x(2*N)
    h=(B-A)/N
    
	if (int(N/2.0)==N/2.0) then
      LS=0
      goto 5
    end if
      LS=3
    ! 3/8 case
    do i=0,3
      w=3
      if(i==0 .or. i==3) then
        w=1
      end if		
      ss=ss+w*func(2*i)!h-0.2
    end do
    ss=ss*h*3/8

    if (N==3) then
      goto 10
    end if
5   do i=LS,N
	  
      w=2
      if (int(i/2.0)*2+1==i) then
        w=4
      end if
      if(i==LS .or. i==N) then
        w=1
      end if
      s=s+w*func(2*i)!h-0.2
    end do
    ss=ss+s*h/3
10  print *, "Results =",ss
 
        
      
end program simpson