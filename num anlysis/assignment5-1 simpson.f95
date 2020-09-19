program simpson	
	implicit none
    real:: h,x(0:100),func(0:100),s,r,A,B,ss
    integer:: maxN,N,i,w,LS
    open(unit=30, file='acceleration.txt', status='unknown')
    open(unit=40, file='velocity.txt', status='unknown')
    
    print *,"How many Sections do you want to calculate with?"
	read *, maxN
    do i=0,maxN
      read (30,*) x(i),func(i)
    end do

do N=3,maxN
    
    ss=0     ! entire sum
    s=0      ! sum within 1/3
    LS=0     ! 0 or 3, (first three intervals)
  
	
    A=x(0)
    B=x(N)
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
      ss=ss+w*func(i)
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
      s=s+w*func(i)
    end do
    ss=ss+s*h/3
10  write (40,*) x(N),ss
 
        
end do
end program simpson