# This comment should be preserved.

# The best way to regenerate this file is open it up
# in the editor. i.e:
#     marimo edit tests/_ast/codegen_data/test_generate_filecontents_toplevel.py

import marimo

with marimo.import_guard():
    # Imports used by your notebook.
    # This section is automatically generated by marimo.
    import io
    import textwrap
    import typing
    from pathlib import Path

    import marimo as mo


__generated_with = "0.0.0"
app = marimo.App(_toplevel_fn=True)


@app.cell
def _(fun_that_uses_another_but_out_of_order):
    shadow = 1
    globe = 1
    (
        fun_that_uses_mo(),
        fun_that_uses_another(),
        fun_that_uses_another_but_out_of_order(),
    )
    return globe, shadow


@app.function
# Sanity check that base case works.
def addition(a, b):
    return a + b


@app.function
def shadow_case(shadow):
    shadow = 2
    return shadow


@app.cell
def _(shadow):
    def reference_case():
        return shadow
    return


@app.cell
def _(globe):
    def global_case():
        global globe
        return globe
    return


@app.function
def fun_that_uses_mo():
    return mo.md("Hello there!")


@app.cell
def fun_that_uses_another_but_out_of_order():
    def fun_that_uses_another_but_out_of_order():
        return fun_that_uses_another()
    return (fun_that_uses_another_but_out_of_order,)


@app.function
def fun_that_uses_another():
    return fun_that_uses_mo()


@app.cell
def _():
    import io
    import textwrap

    # Comments are stripped out.
    import marimo as mo
    return io, mo, textwrap


@app.cell
def _():
    import typing
    from pathlib import Path
    return Path, typing


if __name__ == "__main__":
    app.run()
