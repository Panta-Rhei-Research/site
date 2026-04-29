---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.abs",
  "permalink": "/verify/taulib/docs/book-i-boundary-tau-real-abs/abs/",
  "summary_short": "`def` declaration in `TauLib.BookI.Boundary.TauRealAbs`.",
  "declaration_id": "TauLib.BookI.Boundary.TauRealAbs::TauReal.abs",
  "declaration_slug": "abs",
  "kind": "def",
  "name": "TauReal.abs",
  "module_name": "TauLib.BookI.Boundary.TauRealAbs",
  "module_url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/",
  "source_line_start": 50,
  "source_line_end": 60,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L50-L60",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.TauRealAbs",
        "url": "/verify/taulib/docs/book-i-boundary-tau-real-abs/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L50-L60",
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

- Module: [TauLib.BookI.Boundary.TauRealAbs](/verify/taulib/docs/book-i-boundary-tau-real-abs/)
- Source path: [`TauLib/BookI/Boundary/TauRealAbs.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/TauRealAbs.lean#L50-L60)
- Source range: L50-L60
- Kind: `def`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Absolute value on `TauReal`: pointwise `TauRat.abs` on the
    approximation sequence. -/
```

## Source Excerpt

```lean
def TauReal.abs (a : TauReal) : TauReal :=
  ⟨fun n => (a.approx n).abs⟩

-- ============================================================
-- PART 2: POINTWISE BEHAVIOR AT toRat LEVEL
-- ============================================================

/-- The `n`th approximation of `a.abs` is the TauRat abs of the `n`th
    approximation of `a`. -/
@[simp] theorem TauReal.abs_approx (a : TauReal) (n : Nat) :
    (a.abs).approx n = (a.approx n).abs := rfl
```
