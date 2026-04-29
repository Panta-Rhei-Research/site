---
{
  "projection_kind": "taulib_declaration",
  "title": "NoShrinkProperty",
  "permalink": "/verify/taulib/docs/book-v-gravity-schwarzschild/no-shrink-property/",
  "summary_short": "`structure` declaration in `TauLib.BookV.Gravity.Schwarzschild`.",
  "declaration_id": "TauLib.BookV.Gravity.Schwarzschild::NoShrinkProperty",
  "declaration_slug": "no-shrink-property",
  "kind": "structure",
  "name": "NoShrinkProperty",
  "module_name": "TauLib.BookV.Gravity.Schwarzschild",
  "module_url": "/verify/taulib/docs/book-v-gravity-schwarzschild/",
  "source_line_start": 147,
  "source_line_end": 152,
  "registry_ids": [
    "V.T03"
  ],
  "related_registry_items": [],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L147-L152",
  "formal_status": "defined",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Gravity.Schwarzschild",
        "url": "/verify/taulib/docs/book-v-gravity-schwarzschild/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L147-L152",
        "external": true
      }
    ],
    "meta": {
      "type": "TauLib Declaration",
      "kind": "structure",
      "status": "defined"
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

- Module: [TauLib.BookV.Gravity.Schwarzschild](/verify/taulib/docs/book-v-gravity-schwarzschild/)
- Source path: [`TauLib/BookV/Gravity/Schwarzschild.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Gravity/Schwarzschild.lean#L147-L152)
- Source range: L147-L152
- Kind: `structure`
- Formal status hint: `defined`

## Registry Links

- No Registry IDs were detected in this declaration block.

## Immediate Comment / Docstring

```lean
/-- [V.T03] No-Shrink Theorem: beyond the maturity horizon n*,
    no τ-admissible evolution step can decrease the BH mass index.

    This is the τ-native mass monotonicity principle.

    Consequences:
    - Hawking evaporation is forbidden (mass cannot decrease)
    - Bekenstein area-law entropy = readout, not mass loss implication
    - BH is permanent ontic object (no information loss) -/
```

## Source Excerpt

```lean
structure NoShrinkProperty where
  /-- The BH mass that cannot shrink. -/
  mass : BHMassIndex
  /-- The BH must be mature (beyond maturity horizon). -/
  mature_proof : mass.is_mature = true
  deriving Repr
```
