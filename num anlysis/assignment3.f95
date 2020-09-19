program lagrange
	implicit none
    real:: f(0:100), x(0:100), z, xa,g
    integer:: n,i,j
    
	open(unit=10,file='lagrange.txt',status='old')

    print*, 'what is the point you want?'
    read*, xa
    read(10,*) n

    do i=0,n
      read (10,*) x(i), f(i)
    end do

    g=0
    do i=0,n
      z=f(i)
      do j=0,n
        if (i/=j) then
          z=z*(xa-x(j))/(x(i)-x(j))
        end if 
      end do
      g=g+z
    end do

    print *,g
end program lagrange