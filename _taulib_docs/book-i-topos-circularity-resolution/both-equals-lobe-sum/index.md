---
{
  "projection_kind": "taulib_declaration",
  "title": "both_equals_lobe_sum",
  "permalink": "/verify/taulib/docs/book-i-topos-circularity-resolution/both-equals-lobe-sum/",
  "summary_short": "`theorem` declaration in `TauLib.BookI.Topos.CircularityResolution`.",
  "declaration_id": "TauLib.BookI.Topos.CircularityResolution::both_equals_lobe_sum",
  "declaration_slug": "both-equals-lobe-sum",
  "kind": "theorem",
  "name": "both_equals_lobe_sum",
  "module_name": "TauLib.BookI.Topos.CircularityResolution",
  "module_url": "/verify/taulib/docs/book-i-topos-circularity-resolution/",
  "source_line_start": 370,
  "source_line_end": 379,
  "registry_ids": [],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L370-L379",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookI.Topos.CircularityResolution",
        "url": "/verify/taulib/docs/book-i-topos-circularity-resolution/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L370-L379",
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

- Module: [TauLib.BookI.Topos.CircularityResolution](/verify/taulib/docs/book-i-topos-circularity-resolution/)
- Source path: [`TauLib/BookI/Topos/CircularityResolution.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookI/Topos/CircularityResolution.lean#L370-L379)
- Source range: L370-L379
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- **The central algebraic identity** of paper §7.3
    (Remark `both-equals-one-central`):
    `Both = e_+ + e_- = 1` realised at the `Truth4` level.

    Under the sector encoding (Truth4.toSectorPair), the apex
    `B = Both` corresponds to the partition-of-unity sum
    `e_+_sector + e_-_sector = (1, 1) = T_sector`, i.e. the
    additive sum of the two lobe idempotents in the sector
    bilattice equals the top sector.  This *is* the Hegelian
    "unity of opposites" realised algebraically, and it is the
    ω-germ stabilised value of the Liar. -/
```

## Source Excerpt

```lean
theorem both_equals_lobe_sum :
    Tau.Polarity.SectorPair.add
      (Truth4.toSectorPair T) (Truth4.toSectorPair F) =
    Truth4.toSectorPair T := by
  -- T = (1,1), F = (0,0); their additive sum is (1,1) = T.
  -- (B + N — the diamond complement — is the more interesting
  -- identity, recorded as `spectral_bridge_partition` in
  -- Logic.Explosion; here we record the lobe-symmetric version
  -- under σ-swap.)
  rfl
```
