---
{
  "projection_kind": "taulib_declaration",
  "title": "lt_axiom_verification",
  "permalink": "/corpus/taulib/docs/book-vii-meta-archetypes/lt-axiom-verification/",
  "summary_short": "`theorem` declaration in `TauLib.BookVII.Meta.Archetypes`.",
  "declaration_id": "TauLib.BookVII.Meta.Archetypes::lt_axiom_verification",
  "declaration_slug": "lt-axiom-verification",
  "kind": "theorem",
  "name": "lt_axiom_verification",
  "module_name": "TauLib.BookVII.Meta.Archetypes",
  "module_url": "/corpus/taulib/docs/book-vii-meta-archetypes/",
  "source_line_start": 58,
  "source_line_end": 62,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L58-L62",
  "formal_status": "formalized",
  "declaration_role": "proof obligation",
  "formal_status_label": "formal proof obligation checked",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookVII.Meta.Archetypes",
        "url": "/corpus/taulib/docs/book-vii-meta-archetypes/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L58-L62",
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

- Module: [TauLib.BookVII.Meta.Archetypes](/corpus/taulib/docs/book-vii-meta-archetypes/)
- Source path: [`TauLib/BookVII/Meta/Archetypes.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookVII/Meta/Archetypes.lean#L58-L62)
- Source range: L58-L62
- Kind: `theorem`
- Public role: `proof obligation`
- Formal status hint: `formal proof obligation checked`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [VII.Lxx] LT Axiom Verification: j_τ satisfies all three Lawvere-Tierney axioms.
    LT1 from J_τ being a Grothendieck topology (maximal sieve covers),
    LT2 from J_τ-closure being idempotent (sheafification is idempotent),
    LT3 from J_τ derived from τ³ cylinder basis (finite meets of covers are covers). -/
```

## Source Excerpt

```lean
theorem lt_axiom_verification :
    j_tau.lt1_truth_closed = true ∧
    j_tau.lt2_idempotent = true ∧
    j_tau.lt3_meet_commute = true :=
  ⟨rfl, rfl, rfl⟩
```
