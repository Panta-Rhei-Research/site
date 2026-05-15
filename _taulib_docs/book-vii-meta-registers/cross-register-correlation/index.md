---
{
  "projection_kind": "taulib_declaration",
  "title": "cross_register_correlation",
  "permalink": "/corpus/taulib/docs/book-vii-meta-registers/cross-register-correlation/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Registers`.",
  "declaration_id": "TauLib.BookVII.Meta.Registers::cross_register_correlation",
  "declaration_slug": "cross-register-correlation",
  "kind": "theorem",
  "name": "cross_register_correlation",
  "module_name": "TauLib.BookVII.Meta.Registers",
  "module_url": "/corpus/taulib/docs/book-vii-meta-registers/",
  "source_line_start": 498,
  "source_line_end": 502,
  "registry_ids": [
    "VII.T09"
  ],
  "related_registry_items": [
    {
      "id": "VII.T09",
      "title": "Cross-Register Correlation",
      "url": "/registry/object/VII.T09/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L498-L502",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Registers",
        "url": "/corpus/taulib/docs/book-vii-meta-registers/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L498-L502",
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

- Module: [TauLib.BookVII.Meta.Registers](/corpus/taulib/docs/book-vii-meta-registers/)
- Source path: [`TauLib/BookVII/Meta/Registers.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Registers.lean#L498-L502)
- Source range: L498-L502
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- `VII.T09` — Cross-Register Correlation

## Immediate Comment / Docstring

```lean
/-- [VII.T09] Cross-Register Correlation (ch14). **CONJECTURAL.**
    If φ is a kernel invariant, then its projections to distinct
    registers exhibit non-trivial correlation without causal
    propagation. This is a framework-observation, not derivable
    from Reg_D alone. -/
```

## Source Excerpt

```lean
theorem cross_register_correlation :
    synchronicity.kernel_invariant = true ∧
    synchronicity.cross_register = true ∧
    synchronicity.non_causal = true :=
  ⟨rfl, rfl, rfl⟩
```
