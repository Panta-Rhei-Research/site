---
{
  "projection_kind": "taulib_declaration",
  "title": "cauchyIter",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/cauchy-iter/",
  "summary_short": "`def` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::cauchyIter",
  "declaration_slug": "cauchy-iter",
  "kind": "def",
  "name": "cauchyIter",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 136,
  "source_line_end": 145,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L136-L145",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L136-L145",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L136-L145)
- Source range: L136-L145
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- The **Cauchy iteration** of a self-referential template
    `Φ : Truth4 → Truth4` from seed `s`: `Φ^n(s)`.
    Defined by recursion on `n`. -/
```

## Source Excerpt

```lean
def cauchyIter (Φ : Truth4 → Truth4) : Nat → Truth4 → Truth4
  | 0,     s => s
  | n + 1, s => Φ (cauchyIter Φ n s)

@[simp] theorem cauchyIter_zero (Φ : Truth4 → Truth4) (s : Truth4) :
    cauchyIter Φ 0 s = s := rfl

@[simp] theorem cauchyIter_succ (Φ : Truth4 → Truth4) (n : Nat)
    (s : Truth4) :
    cauchyIter Φ (n + 1) s = Φ (cauchyIter Φ n s) := rfl
```
