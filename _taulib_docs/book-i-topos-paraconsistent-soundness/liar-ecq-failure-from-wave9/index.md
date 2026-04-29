---
{
  "projection_kind": "taulib_declaration",
  "title": "liar_ECQ_failure_from_Wave9",
  "permalink": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/liar-ecq-failure-from-wave9/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.ParaconsistentSoundness`.",
  "declaration_id": "TauLib.BookI.Topos.ParaconsistentSoundness::liar_ECQ_failure_from_Wave9",
  "declaration_slug": "liar-ecq-failure-from-wave9",
  "kind": "theorem",
  "name": "liar_ECQ_failure_from_Wave9",
  "module_name": "TauLib.BookI.Topos.ParaconsistentSoundness",
  "module_url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/",
  "source_line_start": 326,
  "source_line_end": 331,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L326-L331",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.ParaconsistentSoundness",
        "url": "/verify/taulib/docs/book-i-topos-paraconsistent-soundness/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L326-L331",
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

- Module: [TauLib.BookI.Topos.ParaconsistentSoundness](/verify/taulib/docs/book-i-topos-paraconsistent-soundness/)
- Source path: [`TauLib/BookI/Topos/ParaconsistentSoundness.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/ParaconsistentSoundness.lean#L326-L331)
- Source range: L326-L331
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **Liar-ECQ-failure from Wave 9**: the concrete instantiation
    of `non_explosion` via the Liar's stabilisation at `Both = B`
    (Wave 9's `liar_stabilises_at_Both`).

    This is the paper's narrative integration: the ω-germ
    stabilised Liar value `⟦ L ⟧ = B` (Wave 9) combined with
    `B ∧ σB = B ∈ D` (this module) gives the Liar's contradiction
    `L ∧ ¬L` designated status, and the existence of unstabilised
    `q` with `⟦ q ⟧ = N ∉ D` (Wave 9 case (d)) yields the
    designated-preservation failure. -/
```

## Source Excerpt

```lean
theorem liar_ECQ_failure_from_Wave9 :
    -- The Liar's L ∧ ¬L is designated (lands at B = Both)
    IsDesignated (Truth4.meet B (sigmaSwap B)) ∧
    -- An unstabilised q is not designated (lands at N = Neither)
    ¬ IsDesignated N :=
  ⟨meet_B_sigmaSwap_B_designated, not_isDesignated_N⟩
```
