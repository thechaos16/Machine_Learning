function isPrime(n::Int, li::Array)
	if n==1 || n==0
		return 0
	end
	if n==2 || n==3
		return 1
	end
	for i in li
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
		if isPrime(i,li)==1
			cnt+=1
			li = [li;i]
		end
	end
#	println(li)
#	return cnt
	return li
end

function integerFactorization(n::Any,li::Array)
	#println(n)
	factli = []
	for i in li
		if n%i==0
			n = n/i
			if n==1
				return [i]
			end
			factli = [factli;i;integerFactorization(n,li)]
			uniqueFact = duplicateRemove(factli)
			return uniqueFact			
		end
	end
	return 0
end

function duplicateRemove(li::Array)
	uniqueElem = []
	for i in li
		if i in uniqueElem
			continue
		else
			uniqueElem = [uniqueElem;i]
		end
	end
	return uniqueElem
end

#n = 10^8;
#primeLi = primeLessThan(n);
#cnt = 0;
#for i in 2:n
#	if integerFactorization(i,primeLi)==2
#		cnt+=1
#	end
#end
