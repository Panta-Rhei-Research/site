---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.inv",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-inv/inv/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealInv`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealInv::TauReal.inv",
  "declaration_slug": "inv",
  "kind": "def",
  "name": "TauReal.inv",
  "module_name": "TauLib.BookI.Boundary.TauRealInv",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/",
  "source_line_start": 112,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L112-L114",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealInv",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-inv/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L112-L114",
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

- Module: [TauLib.BookI.Boundary.TauRealInv](/verify/taulib/docs/book-i-boundary-tau-real-inv/)
- Source path: [`TauLib/BookI/Boundary/TauRealInv.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealInv.lean#L112-L114)
- Source range: L112-L114
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Pointwise multiplicative inverse on `TauReal`: at each index, invert
    the TauRat approximation when nonzero, fall back to `TauRat.one`
    otherwise.  The fallback value is irrelevant for the Cauchy
    behavior — past the `BoundedAwayFromZero` witness, every index is
    nonzero and we take the genuine TauRat inverse.

    This function is **total** (no hypothesis needed) so that we can
    embed it in `TauReal.div` without carrying hypotheses through the
    definition.  The good cancellation lemmas (`mul_inv_cancel`, etc.)
    do require `BoundedAwayFromZero` as an explicit argument. -/
```

## Source Excerpt

```lean
def TauReal.inv (a : TauReal) : TauReal :=
  ⟨fun n => if h : (a.approx n).is_nonzero then TauRat.inv (a.approx n) h
            else TauRat.one⟩
```
