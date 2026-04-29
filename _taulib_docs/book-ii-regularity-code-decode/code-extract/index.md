---
{
  "projection_kind": "taulib_declaration",
  "title": "code_extract",
  "permalink": "/verify/taulib/docs/book-ii-regularity-code-decode/code-extract/",
  "summary_short": "`def` declaration in `TauLib.BookII.Regularity.CodeDecode`.",
  "declaration_id": "TauLib.BookII.Regularity.CodeDecode::code_extract",
  "declaration_slug": "code-extract",
  "kind": "def",
  "name": "code_extract",
  "module_name": "TauLib.BookII.Regularity.CodeDecode",
  "module_url": "/verify/taulib/docs/book-ii-regularity-code-decode/",
  "source_line_start": 64,
  "source_line_end": 65,
  "registry_ids": [
    "II.D51"
  ],
  "related_registry_items": [
    {
      "id": "II.D51",
      "title": "Code Map",
      "url": "/registry/object/II.D51/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L64-L65",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Regularity.CodeDecode",
        "url": "/verify/taulib/docs/book-ii-regularity-code-decode/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/verify/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L64-L65",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "def",
      "status": "defined"
    }
  },
  "layout": "taulib-doc",
  "lane": "verify",
  "v2_lane": "verify",
  "status": "Canonical",
  "generated_from": "corpus/taulib-projections",
  "projection_version": "v0.1",
  "canonical_source": "Panta-Rhei-Research/taulib",
  "do_not_edit": true,
  "type": "TauLib Declaration"
}
---

## Declaration Projection

This page is generated directly from the pinned TauLib Lean source snapshot. The source excerpt is public because the active TauLib repository is public.

## Source Provenance

- Module: [TauLib.BookII.Regularity.CodeDecode](/verify/taulib/docs/book-ii-regularity-code-decode/)
- Source path: [`TauLib/BookII/Regularity/CodeDecode.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Regularity/CodeDecode.lean#L64-L65)
- Source range: L64-L65
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `II.D51` — Code Map

## Immediate Comment / Docstring

```lean
/-- [II.D51] Code: extract the function value at a given input.
    code_extract(f, k, x) = f(reduce(x, k))

    This is the fundamental "sampling" operation: the code of f at stage k
    is the restriction of f to Z/P_kZ. The CRT coordinates of x are
    (x mod p_1, ..., x mod p_k), and the code records f at each such point. -/
```

## Source Excerpt

```lean
def code_extract (f : TauIdx → Int) (k x : TauIdx) : Int :=
  f (reduce x k)
```
