#module tuto
function perm(a::String,b::String)
	lena = length(a)
	lenb = length(b)
	if lena!=lenb
		return 0
	end
	lia = []
	lib = []
	for i in 1:lena
		lia = [lia;a[i]]
		lib = [lib;b[i]]
	end
	lia = sort(lia)
	lib = sort(lib)
	for i in 1:lena
		if lia[i]!=lib[i]
			return 0
		end
	end
	return 1
end

function relapri(a::Int,b::Int)
	x = max(a,b)
	y = min(a,b)
	if x%y==0
		return 0
	end
	for i in 3:round(sqrt(y))+1
		if y%i==0
			if x%i==0 || x%(y/i)==0
				return 0
			end
		end
	end
	return 1
end

function euler(n::Int)
	cnt=1
	for i in 2:(n-1)
		if relapri(i,n)==1
			#println(i)
			cnt+=1
		end
	end
	return cnt
end

minimum = 1.2
ans = 0
for i in range(1,10000)
	temp = euler(i)
	if perm(string(i),string(temp))==1
		if float(i)/float(temp)<minimum
			minimum = float(i)/float(temp)
			ans = i
		end
	end
end

println(ans)
