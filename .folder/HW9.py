# Задача 40.

df[df['population']<501]['median_house_value'].mean()
206799.95140186916

# Задача 42.

df[df['population']==df['population'].min()]['households'].max()