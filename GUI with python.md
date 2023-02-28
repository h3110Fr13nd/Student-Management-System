
# Tkinter


### ttk

#### ttk.Style()

__Useful Styles and Widgets__

##### Tree View configs

```python

# set ttk theme to "clam" which support the fieldbackground option

style.theme_use("clam")

style.configure("Treeview",

				background="#040f20",

				fieldbackground="#010409",

				foreground="white",

				bordercolor="#30363d",

				font=('arial', 12),

				rowheight=30

				)
```
##### Tree View Heading
```python
# TreeView Heading configs
style.configure("Treeview.Heading",

				background="#040f20",

				fieldbackground="#010409",

				foreground="#d2a8ff",

				font=('arial', 13, 'bold'),

				rowheight=30

				)
				
style.map("Treeview.Heading",

		  background=[('active', '#1d4a70')],

		  foreground=[('active', '#d2a8ff')]

		  )

```

##### Scrollbar
```python

style.configure("Vertical.TScrollbar",

				background="#040f20",

				bordercolor="#0d1117",

				arrowcolor="darkgray",

				)

style.map("Vertical.TScrollbar",

		  background=[('active', 'black')],

		foreground=[('active', 'white')]

			)


```



---
Tags : [[tkinterDND2]] - [[tkinter]]  -  [[ttk]]  -  [[GUI]] 
Links : [[Student Management Project]]  -  [[Student Management System]]

References : 
