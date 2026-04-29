---
{
  "projection_kind": "taulib_declaration",
  "title": "h_tau_zero_divisors",
  "permalink": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/h-tau-zero-divisors/",
  "summary_short": "`theorem` declaration in `TauLib.BookII.Prologue.SplitComplexInterior`.",
  "declaration_id": "TauLib.BookII.Prologue.SplitComplexInterior::h_tau_zero_divisors",
  "declaration_slug": "h-tau-zero-divisors",
  "kind": "theorem",
  "name": "h_tau_zero_divisors",
  "module_name": "TauLib.BookII.Prologue.SplitComplexInterior",
  "module_url": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/",
  "source_line_start": 68,
  "source_line_end": 70,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L68-L70",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookII.Prologue.SplitComplexInterior",
        "url": "/verify/taulib/docs/book-ii-prologue-split-complex-interior/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L68-L70",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "status": "formalized"
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

- Module: [TauLib.BookII.Prologue.SplitComplexInterior](/verify/taulib/docs/book-ii-prologue-split-complex-interior/)
- Source path: [`TauLib/BookII/Prologue/SplitComplexInterior.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookII/Prologue/SplitComplexInterior.lean#L68-L70)
- Source range: L68-L70
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- H_τ has zero divisors: (1+j)(1-j) = 0.
    This encodes bipolar sector orthogonality, not a pathology. -/
```

## Source Excerpt

```lean
theorem h_tau_zero_divisors :
    SplitComplex.mul ⟨1, 1⟩ ⟨1, -1⟩ = ⟨0, 0⟩ := by
  unfold SplitComplex.mul; ext <;> simp
```
