---
{
  "projection_kind": "taulib_declaration",
  "title": "nf_confluence_statement",
  "permalink": "/verify/taulib/docs/book-i-addressability-hinge-integration/nf-confluence-statement/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Addressability.HingeIntegration`.",
  "declaration_id": "TauLib.BookI.Addressability.HingeIntegration::nf_confluence_statement",
  "declaration_slug": "nf-confluence-statement",
  "kind": "theorem",
  "name": "nf_confluence_statement",
  "module_name": "TauLib.BookI.Addressability.HingeIntegration",
  "module_url": "/verify/taulib/docs/book-i-addressability-hinge-integration/",
  "source_line_start": 130,
  "source_line_end": 136,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L130-L136",
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L130-L136",
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
- Source path: [`TauLib/BookI/Addressability/HingeIntegration.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Addressability/HingeIntegration.lean#L130-L136)
- Source range: L130-L136
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Paper Theorem 2 (NF Confluence — Church-Rosser)
    statement-level form**: the τ-kernel rewriting system
    confluence is captured at the deterministic-NF level.

    Concretely: since `normalize` is a deterministic function
    `Program → NormalForm`, any two paths reducing the same
    Program necessarily produce the same NormalForm.  This is the
    structural manifestation of Church-Rosser at the
    deterministic-rewriting level.

    The full diamond-property formulation from the paper requires
    a non-deterministic rewriting relation `→`, which TauLib's
    deterministic `normalize` function already pre-empts: there's
    only one rewriting path, so no diamond confluence question
    arises.  The "modulo Hinge 7 NF confluence" caveats from
    Hinges 5+6 are discharged by exactly this fact: TauLib's
    NF is canonical and computational. -/
```

## Source Excerpt

```lean
theorem nf_confluence_statement (p : Program) :
    -- Applying normalize twice gives the same result (idempotent
    -- on the NormalForm target — deterministic confluence)
    ∀ p₁ p₂ : Program, normalize p = normalize p₁ → normalize p = normalize p₂ →
      normalize p₁ = normalize p₂ := by
  intro _ _ h₁ h₂
  rw [← h₁, h₂]
```
