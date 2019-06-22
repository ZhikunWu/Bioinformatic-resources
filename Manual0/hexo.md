## [hexo](https://hexo.io/zh-cn/index.html)

### Install Node.js
```
$curl https://raw.github.com/creationix/nvm/master/install.sh | sh

or

$ wget -qO- https://raw.githubusercontent.com/creationix/nvm/v0.33.2/install.sh | bash
=> Downloading nvm from git to '/home/wzk/.nvm'
=> Cloning into '/home/wzk/.nvm'...
remote: Counting objects: 6495, done.
remote: Total 6495 (delta 0), reused 0 (delta 0), pack-reused 6495
Receiving objects: 100% (6495/6495), 1.93 MiB | 14.00 KiB/s, done.
Resolving deltas: 100% (4026/4026), done.
Checking connectivity... done.
* (HEAD detached at v0.33.2)
  master
=> Compressing and cleaning up git repository
Counting objects: 6495, done.
Delta compression using up to 40 threads.
Compressing objects: 100% (6451/6451), done.
Writing objects: 100% (6495/6495), done.
Total 6495 (delta 4300), reused 1996 (delta 0)

=> Appending nvm source string to /home/wzk/.bashrc
=> Appending bash_completion source string to /home/wzk/.bashrc
=> Close and reopen your terminal to start using nvm or run the following to use it now:

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

```

### restart the terminal and run the following command to install Node.js
```
nvm install stable
```

### Install Hexo
Once all the requirements are installed, you can install Hexo with npm
```
$npm install -g hexo-cli

/home/wzk/.nvm/versions/node/v8.2.1/bin/hexo -> /home/wzk/.nvm/versions/node/v8.2.1/lib/node_modules/hexo-cli/bin/hexo

> dtrace-provider@0.8.3 install /home/wzk/.nvm/versions/node/v8.2.1/lib/node_modules/hexo-cli/node_modules/dtrace-provider
> node scripts/install.js


> hexo-util@0.6.1 postinstall /home/wzk/.nvm/versions/node/v8.2.1/lib/node_modules/hexo-cli/node_modules/hexo-util
> npm run build:highlight


> hexo-util@0.6.1 build:highlight /home/wzk/.nvm/versions/node/v8.2.1/lib/node_modules/hexo-cli/node_modules/hexo-util
> node scripts/build_highlight_alias.js > highlight_alias.json

npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.1.2 (node_modules/hexo-cli/node_modules/fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.1.2: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

+ hexo-cli@1.0.3
added 217 packages in 81.758s

```

### init a blog
```
$ hexo init wzk_blog
INFO  Cloning hexo-starter to ~/wzk_blog
Cloning into '/home/wzk/wzk_blog'...
remote: Counting objects: 59, done.
remote: Total 59 (delta 0), reused 0 (delta 0), pack-reused 59
Unpacking objects: 100% (59/59), done.
Checking connectivity... done.
Submodule 'themes/landscape' (https://github.com/hexojs/hexo-theme-landscape.git) registered for path 'themes/landscape'
Cloning into 'themes/landscape'...
remote: Counting objects: 785, done.
remote: Total 785 (delta 0), reused 0 (delta 0), pack-reused 785
Receiving objects: 100% (785/785), 2.54 MiB | 114.00 KiB/s, done.
Resolving deltas: 100% (403/403), done.
Checking connectivity... done.
Submodule path 'themes/landscape': checked out 'decdc2d9956776cbe95420ae94bac87e22468d38'
INFO  Install dependencies
npm WARN deprecated swig@1.4.2: This package is no longer maintained
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: cssstyle@0.2.37 (node_modules/cssstyle):
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: sha1-VBCXI0yyUTyDzu06zdwn/yeYfVQ= integrity checksum failed when using sha1: wanted sha1-VBCXI0yyUTyDzu06zdwn/yeYfVQ= but got sha1-tD1G3B4N2xl7yTMQceaa1fIFlg8=. (29656 bytes)

npm ERR! code ECONNRESET
npm ERR! errno ECONNRESET
npm ERR! network request to https://registry.npmjs.org/css-parse/-/css-parse-1.7.0.tgz failed, reason: socket hang up
npm ERR! network This is a problem related to network connectivity.
npm ERR! network In most cases you are behind a proxy or have bad network settings.
npm ERR! network 
npm ERR! network If you are behind a proxy, please make sure that the
npm ERR! network 'proxy' config is set properly.  See: 'npm help config'

npm ERR! A complete log of this run can be found in:
npm ERR!     /home/wzk/.npm/_logs/2017-07-31T05_35_21_429Z-debug.log
WARN  Failed to install dependencies. Please run 'npm install' manually!

```

### starting the server
```
wzk@ubuntu 01:42:49 O_O /home/wzk/wzk_blog 
$ npm install hexo --save
$ hexo server --draft --open
```

### hexo command
```
$ hexo server --draft --open
Usage: hexo <command>

Commands:
  clean     Remove generated files and cache.
  config    Get or set configurations.
  deploy    Deploy your website.
  generate  Generate static files.
  help      Get help on a command.
  init      Create a new Hexo folder.
  list      List the information of the site
  migrate   Migrate your site from other system to Hexo.
  new       Create a new post.
  publish   Moves a draft post from _drafts to _posts folder.
  render    Render files with renderer plugins.
  version   Display version information.

Global Options:
  --config  Specify config file instead of using _config.yml
  --cwd     Specify the CWD
  --debug   Display all verbose messages in the terminal
  --draft   Display draft posts
  --safe    Disable all plugins and scripts
  --silent  Hide output on console

For more help, you can use 'hexo help [command]' for the detailed information
or you can check the docs: http://hexo.io/docs/
```

### creat a blog
```
$ hexo new draft 'Use of Pfam'
INFO  Created: ~/wzk_blog/source/_drafts/Use-of-Pfam.md
wzk@ubuntu 01:48:37 ^_^ /home/wzk/wzk_blog 
$ vi ~/wzk_blog/source/_drafts/Use-of-Pfam.md


$ hexo publish Use-of-Pfam
INFO  Published: ~/wzk_blog/source/_posts/Use-of-Pfam.md



$ hexo generate
INFO  Start processing
INFO  Files loaded in 148 ms
INFO  Generated: css/style.styl
INFO  Generated: fancybox/blank.gif
INFO  Generated: fancybox/jquery.fancybox.css
INFO  Generated: fancybox/fancybox_loading.gif
INFO  Generated: fancybox/jquery.fancybox.pack.js
INFO  Generated: fancybox/fancybox_sprite.png
INFO  Generated: fancybox/fancybox_sprite@2x.png
INFO  Generated: fancybox/jquery.fancybox.js
INFO  Generated: fancybox/fancybox_overlay.png
INFO  Generated: fancybox/fancybox_loading@2x.gif
INFO  Generated: css/fonts/fontawesome-webfont.ttf
INFO  Generated: css/fonts/fontawesome-webfont.svg
INFO  Generated: fancybox/helpers/jquery.fancybox-buttons.css
INFO  Generated: js/script.js
INFO  Generated: fancybox/helpers/jquery.fancybox-buttons.js
INFO  Generated: fancybox/helpers/jquery.fancybox-thumbs.css
INFO  Generated: fancybox/helpers/fancybox_buttons.png
INFO  Generated: fancybox/helpers/jquery.fancybox-thumbs.js
INFO  Generated: fancybox/helpers/jquery.fancybox-media.js
INFO  Generated: css/fonts/fontawesome-webfont.eot
INFO  Generated: css/fonts/fontawesome-webfont.woff
INFO  Generated: css/fonts/FontAwesome.otf
INFO  Generated: css/images/banner.jpg
INFO  23 files generated in 24 ms

```

### build relationship to git
```
$ npm install hexo-deployer-git --save
npm WARN optional SKIPPING OPTIONAL DEPENDENCY: fsevents@1.1.2 (node_modules/fsevents):
npm WARN notsup SKIPPING OPTIONAL DEPENDENCY: Unsupported platform for fsevents@1.1.2: wanted {"os":"darwin","arch":"any"} (current: {"os":"linux","arch":"x64"})

+ hexo-deployer-git@0.3.1
added 132 packages in 81.553s

```
### install the server
```
npm install hexo-server --save
```



## theme
* [hexo-theme-next](hexo-theme-next)
* [hexo-theme-yilia](https://github.com/litten/hexo-theme-yilia)
* [Casper](https://github.com/TryGhost/Casper)
* [jacman](https://github.com/wuchong/jacman)
* [hexo-theme-formula](https://github.com/bubkoo/hexo-theme-formula)



