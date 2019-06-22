#From gpratt
def plot_go_enrichment(df, filter_value=None, **kwargs):
	new_index = []
	for index, description in izip(df.index, df['GO Term Description']):
		new_index.append(list(index[:-1]) + [description])
	df.index = pd.MultiIndex.from_tuples(new_index)
	go_matrix = df['Bonferroni-corrected Hypergeometric p-Value'].apply(lambda x: -1 * np.log10(x))
	go_matrix = go_matrix.unstack(range(len(go_matrix.index.levels) - 1))
	go_matrix = go_matrix.fillna(0)
	if filter_value is not None:
		go_matrix = go_matrix[go_matrix.apply(max, axis=1) > filter_value]
    sns.clustermap(go_matrix, robust=True, **kwargs)
	
