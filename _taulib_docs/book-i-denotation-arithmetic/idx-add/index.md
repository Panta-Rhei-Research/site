---
{
  "projection_kind": "taulib_declaration",
  "title": "idx_add",
  "permalink": "/verify/taulib/docs/book-i-denotation-arithmetic/idx-add/",
  "summary_short": "`def` declaration in `TauLib.BookI.Denotation.Arithmetic`.",
  "declaration_id": "TauLib.BookI.Denotation.Arithmetic::idx_add",
  "declaration_slug": "idx-add",
  "kind": "def",
  "name": "idx_add",
  "module_name": "TauLib.BookI.Denotation.Arithmetic",
  "module_url": "/verify/taulib/docs/book-i-denotation-arithmetic/",
  "source_line_start": 46,
  "source_line_end": 47,
  "registry_ids": [
    "I.D10"
  ],
  "related_registry_items": [
    {
      "id": "I.D10",
      "title": "Index Addition",
      "url": "/registry/object/I.D10/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L46-L47",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Denotation.Arithmetic",
        "url": "/verify/taulib/docs/book-i-denotation-arithmetic/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L46-L47",
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

- Module: [TauLib.BookI.Denotation.Arithmetic](/verify/taulib/docs/book-i-denotation-arithmetic/)
- Source path: [`TauLib/BookI/Denotation/Arithmetic.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Denotation/Arithmetic.lean#L46-L47)
- Source range: L46-L47
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- `I.D10` — Index Addition

## Immediate Comment / Docstring

```lean
/-- [I.D10] Index addition: the depth after m applications of ρ to ⟨α, n⟩.
    This *earns* addition from the iterator. -/
```

## Source Excerpt

```lean
def idx_add (n m : TauIdx) : TauIdx :=
  (iter_rho m (toAlphaOrbit n)).depth
```
