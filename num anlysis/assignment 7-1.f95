program gauss_seidel
	implicit none
    integer :: i,n,j,rmax,row,pivot,times,temp
    real:: a(50,50), soln(50)

    open(unit=10,file="G_input.txt",status="unknown")
    open(unit=20,file="G_output_Seidel.txt",status="unknown")

    n=3

    do i=1,3
      read(10,*) a(i,1),a(i,2),a(i,3),a(i,4)
    end do

    do pivot=1,n-1
      rmax=pivot
      do row=pivot ,n
        if (abs(a(rmax,pivot))<abs(a(row,pivot))) then 
          rmax=row
        end if
      end do
      if (rmax /=pivot) then
        do j=1,n+1
          temp=a(rmax,j)
          a(rmax,j)=a(pivot,j)
          a(pivot,j)=temp
        end do
      end if
    end do

    call gauss_seidel_sub(a,n,times,soln)


    print*, "Number of iterations:", times

    do i=1,3
      print 33,i,soln(i)
      write (20,*) soln(i)
    end do
33  format(5x,"x",i1,"=",f10.5)

end program gauss_seidel

Subroutine gauss_seidel_sub(a,times,n,soln)
	implicit none
    integer:: i,n,j,Times
    real:: tol,errmax,a(50,50),sum1,xnew,error,soln(50)
    
	tol=0.0001
	errmax=tol+1.0
    Times=0

    n=3
    do i=1,n
      soln(i)=0.0
    end do

15  if (errmax>tol) then
      errmax=0
      do i=1,n
        sum1=0.0
        do j =1,n
          if(j/= i) then 
            sum1=sum1+ a(i,j)*soln(j)
          end if
        end do

        xnew=(a(i,4)-sum1)/a(i,i)
        error= abs(xnew-soln(i))

        if (error>errmax) then
          errmax=error
        end if
        soln(i)=xnew
      end do
      Times=Times+1
      goto 15
    end if

  
        
end subroutine gauss_seidel_sub
