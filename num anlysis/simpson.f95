program simpson	
	implicit none
    real:: h,x,s,r,A,B,ss
    integer:: N,i,w,LS
3   print *,"How many Sections do you want to calculate with?"
	read *, N
    print*,"what's the starting section?"
    read*, A
    print *,"what's the ending section?"
    read *, B
    ss=0     ! entire sum
    s=0      ! sum within 1/3
    LS=0     ! 0 or 3, (first three intervals)
! Eliminating N<3 cases
	if (N<3) then
      print *,"IMPOSSIBLE!!"
      go to 3
    end if
! case Determination
	h= (B-A)/N
    if (int(N/2.0)==N/2.0) then
      LS=0
      goto 5
    end if
      LS=3
    do i=0,3
      x=A+h*i
      w=3
      if(i==0 .or. i==3) then
        w=1
      end if
      ss=ss+w*func(x)
    end do
    ss=ss*h*3/8

    if (N==3) then
      goto 10
    end if
5   do i=0,N-LS
	  x=A+h*(i+LS)
      w=2
      if (int(i/2.0)*2+1==i) then
        w=4
      end if
      if(i==0 .or. i==N-LS) then
        w=1
      end if
      s=s+w*func(x)
    end do
    ss=ss+s*h/3
10  print *, "Results =",ss
	contains
    	Function func(x)
        real:: x,func
        	func=(1+(x/2))
        end function
        
      
end program simpson