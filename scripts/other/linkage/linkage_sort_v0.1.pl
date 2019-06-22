#!/usr/bin/perl -w


###usage:  perl linkage_sort_v0.1.pl linkage_input.txt linkage_out ######
open IN,"< $ARGV[0]"; ## linkage_input.txt
open OUT, "> $ARGV[1]";

my %genet_info;
my %snp_line;
while (my $line=<IN>){
	chomp($line);
	my ($snp,$genetic,$chr,$physical)= split("\t",$line);
	push (@{$genet_info{$genetic}},$line);
	$snp_line{$snp} = $line;
}
close IN;

my %chr_phy_snp;
my(@chrs,@randoms,@NAs);
foreach my $h_genet (sort {$a<=>$b} keys %genet_info){
	
	for(my $i=0;$i<=$#{$genet_info{$h_genet}};$i++){
		my $line = ${$genet_info{$h_genet}}[$i];
		my ($snp,$genetic,$chr,$physical) = split("\t",$line);
		my $chr_phy = join(":",$snp,$chr,$physical);
		$chr_phy_snp{$chr_phy} = $line;
		if($chr =~ m/^chr.*[0-9]$/){
			push (@chrs,$chr_phy);
		}elsif($chr =~ m/random$/){
			push (@randoms,$chr_phy);
		}elsif($chr eq "NA"){ ##may mutiple NA
			push (@NAs,$chr_phy);
		}
	}
	my %pos_snp;
	my @physicals;
	my ($index_m,$phy_m,$snp_m);
	if (@chrs){
		for(my $j=0;$j<=$#chrs;$j++){
			my ($snp_c,$chr_c,$phy_c) = split(":",$chrs[$j]);
			$pos_snp{$phy_c}=$snp_c;
			push (@physicals,$phy_c);
		}
		$index_m = &median_index(@physicals);
		$phy_m = $physicals[$index_m];
		$snp_m = $pos_snp{$phy_m};
		print OUT $snp_line{$snp_m}."\n";
		undef %pos_snp;
		undef @physicals;
	}else{
		if (@randoms){
			for(my $j=0;$j<=$#randoms;$j++){
				my ($snp_c,$chr_c,$phy_c) = split(":",$randoms[$j]);
				$pos_snp{$phy_c}=$snp_c;
				push (@physicals,$phy_c);
			}	
			$index_m = &median_index(@physicals);
			$phy_m = $physicals[$index_m];
			$snp_m = $pos_snp{$phy_m};
			print OUT $snp_line{$snp_m}."\n";
			undef %pos_snp;
			undef @physicals;
		}else{
			if (@NAs){
				print OUT $chr_phy_snp{$NAs[0]}."\n";
			}
		}
	}
	undef @chrs;
	undef @randoms;
	undef @NAs;
}




sub median_index{
	my @values = @_;
	my %value_index;
	for(my $p=0;$p<=$#values;$p++){
		$value_index{$values[$p]} = $p;
	}

	my @sorted_value = sort {$a <=> $b} @values;
	if (($#sorted_value+1)%2 == 0){
		my $media = $sorted_value[0] + $sorted_value[$#sorted_value];
		if (abs($sorted_value[($#sorted_value+1)/2 -1] - $media) < abs($sorted_value[($#sorted_value+1)/2] - $media) ){
			return $value_index{$sorted_value[($#sorted_value+1)/2 -1]};
		}else {
			return $value_index{$sorted_value[($#sorted_value+1)/2]};
		}
	}else {
		return $value_index{$sorted_value[int(($#sorted_value+1)/2)]};
	}

}
