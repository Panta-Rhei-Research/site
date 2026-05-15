---
{
  "projection_kind": "taulib_declaration",
  "title": "internal_logic_four_valued",
  "permalink": "/corpus/taulib/docs/book-i-topos-earned-topos/internal-logic-four-valued/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.EarnedTopos`.",
  "declaration_id": "TauLib.BookI.Topos.EarnedTopos::internal_logic_four_valued",
  "declaration_slug": "internal-logic-four-valued",
  "kind": "theorem",
  "name": "internal_logic_four_valued",
  "module_name": "TauLib.BookI.Topos.EarnedTopos",
  "module_url": "/corpus/taulib/docs/book-i-topos-earned-topos/",
  "source_line_start": 187,
  "source_line_end": 189,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L187-L189",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.EarnedTopos",
        "url": "/corpus/taulib/docs/book-i-topos-earned-topos/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L187-L189",
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

- Module: [TauLib.BookI.Topos.EarnedTopos](/corpus/taulib/docs/book-i-topos-earned-topos/)
- Source path: [`TauLib/BookI/Topos/EarnedTopos.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/EarnedTopos.lean#L187-L189)
- Source range: L187-L189
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- Internal logic: the topos has 4 truth values, not 2.
    This means the internal logic is both:
    - Intuitionistic (not all propositions are decidable: B, N exist)
    - Paraconsistent (contradictions don't explode: I.T13) -/
```

## Source Excerpt

```lean
theorem internal_logic_four_valued :
    ∀ v : Omega_tau, v = T ∨ v = F ∨ v = B ∨ v = N :=
  omega_tau_classifier
```
