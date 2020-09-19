program Laplace_equation
 	implicit none
    integer::i,j,numit
    real::h(1000,1000),k1,k2,amax,oldval,err,A,B

    open(unit=10,file="Laplace_output1.txt",status="unknown")

    k1=0.00003
    k2=0.000008
    !all set to 20
	do i=1,701
       do j=1,141
         h(i,j)=20
       end do
    end do
    !rock=0
    do i=302,400
      do j=82,141
        h(i,j)=0
      end do
    end do
    !constant boundary set to 30 or 10
	do i=1,301
    	h(i,1)=30
    end do

    do i=401,701
    	h(i,1)=10
    end do
    
    do j=1,141
    	h(1,j)=30
        h(701,j)=10
    end do
    	

    numit=0
35  amax=0
    numit=numit+1
	
    !impermeable boundary 1
	do i=302,400
      oldval=h(i,1)
      h(i,1)=(h(i-1,1)+h(i+1,1)+2*h(i,2))/4
      err=ABS(h(i,1)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do

    !impermeable boundary 2
	do i=2,300
      oldval=h(i,141)
      h(i,141)=(h(i-1,141)+h(i+1,141)+2*h(i,140))/4
      err=ABS(h(i,141)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do

    h(301,141)=(2*h(300,141)+2*h(301,140))/4

    !impermeable boundary 3
	do j=82,140
    	oldval=h(301,j)
    	h(301,j)=(h(301,j-1)+h(301,j+1)+2*h(300,j))/4
        err=ABS(h(301,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do
    
	h(301,81)=(h(300,81)+h(302,81)+h(301,80)+h(301,82))/4

    !impermeable boundary 4
	do i=302,400
    oldval=h(i,81)
      h(i,81)=(h(i-1,81)+h(i+1,81)+2*h(i,80))/4
      err=ABS(h(i,81)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do
    
	h(401,81)=(h(400,81)+h(402,81)+h(401,80)+h(401,82))/4

    !impermeable boundary 5
	do j=82,140
        oldval=h(401,j)
    	h(401,j)=(h(401,j-1)+h(401,j+1)+2*h(402,j))/4
        err=ABS(h(401,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do
    
	h(401,141)=(2*h(402,141)+2*h(401,140))/4

    !impermeable boundary 6
	do i=402,700
       oldval=h(i,141)
       h(i,141)=(h(i-1,141)+h(i+1,141)+2*h(i,140))/4
       err=ABS(h(i,141)-oldval)
        if (err>= amax) then
          amax=err
        end if
    end do




	!Area1
    do i=2,300
      do j=2,40
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do
    !k1,k2 boundary1
    do i=2,300
      oldval=h(i,41)
      h(i,41)=(h(i-1,41)+h(i+1,41)+2*k1*h(i,40)/(k1+k2)+2*k2*h(i,42)/(k1+k2))/4
      err=ABS(h(i,41)-oldval)
      if (err>= amax) then
          amax=err
      end if
    end do
    !Area2
    do i=2,300
      do j=42,140
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do
	!Area3
    do i=301,401
      do j=2,40
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do

    !k1,k2 boundary2
    do i=301,401
      oldval=h(i,41)
      h(i,41)=(h(i-1,41)+h(i+1,41)+2*k1*h(i,40)/(k1+k2)+2*k2*h(i,42)/(k1+k2))/4
      err=ABS(h(i,41)-oldval)
      if (err>= amax) then
          amax=err
      end if
    end do

    !Area4
    do i=301,401
      do j=41,80
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do

    !Area5
    do i=402,700
      do j=2,40
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do

    !k1,k2 boundary3
    do i=402,700
      oldval=h(i,41)
      h(i,41)=(h(i-1,41)+h(i+1,41)+2*k1*h(i,40)/(k1+k2)+2*k2*h(i,42)/(k1+k2))/4
      err=ABS(h(i,41)-oldval)
      if (err>= amax) then
          amax=err
      end if
    end do
    
    !Area6
    do i=402,700
      do j=42,140
        oldval=h(i,j)
        h(i,j)=(h(i-1,j)+h(i+1,j)+h(i,j-1)+h(i,j+1))/4
        err=ABS(h(i,j)-oldval)
        if (err>= amax) then
          amax=err
        end if
      end do
    end do

    


	A=h(321,61)
    B=h(421,21)
    print *,"Number of iteration is", numit
    print *,"amax is", amax
	print *,"A is",A
    print *,"b is",B

    if (amax>=0.01) then
      goto 35
    end if

    write (10,100) ((h(i,j),i=1,701),j=1,141)

100 format(141(701f10.4/))    


    
    
end program 