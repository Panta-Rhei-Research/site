---
{
  "projection_kind": "taulib_declaration",
  "title": "CauchyTauReal.mul_respects_equiv",
  "permalink": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/mul-respects-equiv/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealQuotient::CauchyTauReal.mul_respects_equiv",
  "declaration_slug": "mul-respects-equiv",
  "kind": "theorem",
  "name": "CauchyTauReal.mul_respects_equiv",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "source_line_start": 149,
  "source_line_end": 153,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L149-L153",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
        "url": "/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L149-L153",
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealQuotient](/verify/taulib/docs/book-i-boundary-bridge-tau-real-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L149-L153)
- Source range: L149-L153
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
No immediate Lean doc/comment block was detected for this declaration.
```

## Source Excerpt

```lean
theorem CauchyTauReal.mul_respects_equiv (a₁ a₂ b₁ b₂ : CauchyTauReal)
    (ha : equiv a₁ a₂) (hb : equiv b₁ b₂) :
    equiv (a₁.mul b₁) (a₂.mul b₂) :=
  TauReal.mul_respects_equiv_under_cauchy a₁.val a₂.val b₁.val b₂.val
    a₂.isCauchy b₁.isCauchy ha hb
```
