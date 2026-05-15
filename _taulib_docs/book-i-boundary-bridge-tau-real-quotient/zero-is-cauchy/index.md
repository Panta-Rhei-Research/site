---
{
  "projection_kind": "taulib_declaration",
  "title": "TauReal.zero_isCauchy",
  "permalink": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/zero-is-cauchy/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Boundary.Bridge.TauRealQuotient`.",
  "declaration_id": "TauLib.BookI.Boundary.Bridge.TauRealQuotient::TauReal.zero_isCauchy",
  "declaration_slug": "zero-is-cauchy",
  "kind": "theorem",
  "name": "TauReal.zero_isCauchy",
  "module_name": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
  "module_url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/",
  "source_line_start": 53,
  "source_line_end": 61,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L53-L61",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Boundary.Bridge.TauRealQuotient",
        "url": "/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/"
      },
      {
        "title": "TauLib Projection Index",
        "url": "/corpus/taulib/docs/"
      },
      {
        "title": "Formalization Status",
        "url": "/verify/taulib/status/"
      }
    ],
    "artifacts": [
      {
        "title": "Source on GitHub",
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L53-L61",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "theorem",
      "role": "proof obligation",
      "status": "formal proof obligation checked"
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

- Module: [TauLib.BookI.Boundary.Bridge.TauRealQuotient](/corpus/taulib/docs/book-i-boundary-bridge-tau-real-quotient/)
- Source path: [`TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Boundary/Bridge/TauRealQuotient.lean#L53-L61)
- Source range: L53-L61
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
-- ============================================================
-- PART 1: TauReal.zero / TauReal.one are Cauchy
-- ============================================================
```

## Source Excerpt

```lean
theorem TauReal.zero_isCauchy : TauReal.zero.IsCauchy :=
  ⟨fun _ => 0, fun k _ _ _ _ => by
    show TauRat.lt _ _
    unfold TauRat.lt
    rw [TauRat.toRat_abs, toRat_sub]
    show |TauRat.zero.toRat - TauRat.zero.toRat| < (TauRat.ofNatRecip k).toRat
    rw [toRat_zero]
    simp
    exact TauRat.ofNatRecip_pos k⟩
```
