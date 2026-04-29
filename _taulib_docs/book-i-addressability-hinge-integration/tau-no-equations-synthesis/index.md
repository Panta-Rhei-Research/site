---
{
  "projection_kind": "taulib_declaration",
  "title": "tau_no_equations_synthesis",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/tau-no-equations-synthesis/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::tau_no_equations_synthesis",
  "declaration_slug": "tau-no-equations-synthesis",
  "kind": "theorem",
  "name": "tau_no_equations_synthesis",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 231,
  "source_line_end": 236,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L231-L236",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Addressability.HingeIntegration",
        "url": "/verify/taulib/docs/book-i-addressability-hinge-integration/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L231-L236",
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

- Module: [TauLib.BookI.Addressability.HingeIntegration](/verify/taulib/docs/book-i-addressability-hinge-integration/)
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L231-L236)
- Source range: L231-L236
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 6 corollary — no equations in classical sense**:
    the assertion that `tauEq` is fully reducible to NF comparison
    means the τ-framework has no "free-standing" equations beyond
    address resolution.

    Numerical witness: at the Program level, two specific programs
    are tauEq iff their NormalForms have ontic distance zero
    (i.e. are NF-equivalent componentwise).  This computational
    fact is the core of the paper's "Category τ has no equations"
    thesis. -/
```

## Source Excerpt

```lean
theorem tau_no_equations_synthesis (a b : Program) :
    -- The structural equivalence of tauEq with ontic-distance zero
    (tauEq a b ↔ OnticDist (normalize a) (normalize b) = 0) ∧
    -- Reflexivity
    tauEq a a :=
  ⟨address_resolution_theorem a b, tauEq_refl a⟩
```
