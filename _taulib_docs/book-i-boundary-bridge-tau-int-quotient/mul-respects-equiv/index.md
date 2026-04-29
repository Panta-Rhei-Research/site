---
{
  "projection_kind": "taulib_declaration",
  "title": "TauInt.mul_respects_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/mul-respects-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauIntQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauIntQuotient::TauInt.mul_respects_equiv",
  "declaration_slug": "mul-respects-equiv",
  "kind": "theorem",
  "name": "TauInt.mul_respects_equiv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/",
  "source_line_start": 110,
  "source_line_end": 114,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L110-L114",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauIntQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L110-L114",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauIntQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-int-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauIntQuotient.lean#L110-L114)
- Source range: L110-L114
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- `mul` respects equiv. -/
```

## Source Excerpt

```lean
theorem TauInt.mul_respects_equiv (a₁ a₂ b₁ b₂ : TauInt)
    (ha : TauInt.equiv a₁ a₂) (hb : TauInt.equiv b₁ b₂) :
    TauInt.equiv (a₁.mul b₁) (a₂.mul b₂) := by
  rw [equiv_iff_toInt_eq] at ha hb ⊢
  rw [toInt_mul, toInt_mul, ha, hb]
```
