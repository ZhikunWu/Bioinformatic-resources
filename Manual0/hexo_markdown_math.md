# hexo中使用数学公式

<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>

hexo中多用markdown写作，本人直接在sublime 3中使用markdown，因此需要在sublime中安装公式渲染的插件。
同时在hexo展示的时候也要对相应的插件进行配置。

## Sublime的Markdown中用 MathJax 写数学公式


### [sublime中安装mathjax插件](https://reginald1787.github.io/2014/06/29/sublime-markdown-mathjax/)
Sublime 中是用 OmniMarkupPreviewer 来写 Markdown 的，简单好用，而且实时处理。

OmniMarkupPreviewer 的安装方法最简单是通过 Sublime Package Control ：


* 先安装 Package Control (如果没有的话)
* Ctrl/Command + Shift + P 打开 Package Control, 选择 Install Package
* 找到 OmniMarkupPreview 安装

在Markdown中主要是通过 MathJax 来写公式：

在 Sublime 的 OmniMarkupPreviewer 的设置里设置为 mathjax_enabled = true

### Markdown书写公式
在Markdown中书写公式时，需要加上以下语句：
```
<script type="text/javascript"
   src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
```



## [Hexo使用hexo-math插件支持MathJax](http://zjubank.com/2016/08/16/hexo-use-mathjax/)


MathJax是使用LaTeX方式输入数学公式的好工具。Hexo虽然可以直接使用mathjax，但是存在一些不方便之处。使用hexo-math这个插件可以大大方便使用。

### hexo中安装math插件
在hexo安装目录下执行
```
npm install hexo-math --save
```

### 修改根目录下的配置文件
然后编辑站点根目录下的`_config.yml`，添加
```
math:
  engine: 'mathjax' # or 'katex'
  # mathjax:
  #   src: custom_mathjax_source
```

### 修改theme中的配置文件

之后进入theme的目录，本人theme是yalia，进入该文件夹，编辑主题的_config.yml，找到mathjax字段。yalia中默认mathjax是禁用，需要改成

```
mathjax:
   enable: true
```

最后hexo g，就可以部署或者运行server查看效果了。

如果此时仍没有看到预期的效果，请看下一步。


## [处理Hexo和MathJax的兼容问题](http://hongyitong.github.io/2016/10/24/%E5%A6%82%E4%BD%95%E5%9C%A8Hexo%E4%B8%AD%E4%BD%BF%E7%94%A8MathJax/)

简单来说，要让你的Hexo支持MathJax渲染公式，你只需要使用两条命令：
To fully support MathJax in your Hexo blog, you can simply use the following commands:
```
npm uninstall hexo-renderer-marked --save
npm install hexo-renderer-kramed --save
```

第一条命令用于卸载 hexo-renderer-marked（注意，如果你使用了其他的渲染插件，请卸载对应的插件），它是hexo自带的Markdown渲染引擎。

第二条命令用于安装 hexo-renderer-kramed 插件，这个渲染插件针对MathJax支持进行了改进。安装完成后，重新生成博客就会惊喜地发现你的公式已经能够正常显示了。

安装完以后，先 hexo clean && hexo g 重新生成静态网页，然后 hexo s 查看，这回公式能正常显示了。




## [MathJax语法](http://waterbolik.github.io/jekyll/2015/10/14/MathJax%E8%AF%AD%E6%B3%95%E8%AF%A6%E8%A7%A3)
MathJax语法可以看考 [MathJax语法详解](http://waterbolik.github.io/jekyll/2015/10/14/MathJax%E8%AF%AD%E6%B3%95%E8%AF%A6%E8%A7%A3)


例如：
```
$$\color{black}{ G = 2 * \sum _{i=1} ^4 n _i * ln(\frac {obs(n _i)} {exp(n _i)}) } $$
```

生成结果为：
$$\color{black}{ G = 2 * \sum _{i=1} ^4 n _i * ln(\frac {obs(n _i)} {exp(n _i)}) } $$


