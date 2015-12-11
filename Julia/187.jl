function isPrime(n::Int)
	if n==1 || n==0
		return 0
	end
	if n==2 || n==3
		return 1
	end
	for i in 2:round(sqrt(n))+1
		if n%i==0
			return 0
		end
	end
	return 1
end

function primeLessThan(n::Int)
	cnt = 0
	li = []
	for i in 2:n
		if isPrime(i)==1
			cnt+=1
			li = [li;i]
		end
	end
#	println(li)
#	return cnt
	return li
end

function integerFactorization(n::Any,li::Array)
	println(n)
	factli = []
	for i in li
		if n%i==0
			n = n/i
			if n==1
				return [i]
			end
			factli = [factli;i;integerFactorization(n,li)]
			return factli			
		end
	end
	return 0
end
