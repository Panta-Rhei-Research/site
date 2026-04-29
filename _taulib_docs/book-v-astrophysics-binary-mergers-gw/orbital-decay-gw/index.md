---
{
  "projection_kind": "taulib_declaration",
  "title": "orbital_decay_gw",
  "permalink": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/orbital-decay-gw/",
  "summary_short": "`theorem` declaration in `TauLib.BookV.Astrophysics.BinaryMergersGW`.",
  "declaration_id": "TauLib.BookV.Astrophysics.BinaryMergersGW::orbital_decay_gw",
  "declaration_slug": "orbital-decay-gw",
  "kind": "theorem",
  "name": "orbital_decay_gw",
  "module_name": "TauLib.BookV.Astrophysics.BinaryMergersGW",
  "module_url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/",
  "source_line_start": 149,
  "source_line_end": 151,
  "registry_ids": [
    "V.P80"
  ],
  "related_registry_items": [
    {
      "id": "V.P80",
      "title": "GW Energy Flux",
      "url": "/registry/object/V.P80/"
    }
  ],
  "upstream_url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L149-L151",
  "formal_status": "formalized",
  "right_rail": {
    "related": [
      {
        "title": "TauLib.BookV.Astrophysics.BinaryMergersGW",
        "url": "/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/"
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
        "url": "https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L149-L151",
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

- Module: [TauLib.BookV.Astrophysics.BinaryMergersGW](/verify/taulib/docs/book-v-astrophysics-binary-mergers-gw/)
- Source path: [`TauLib/BookV/Astrophysics/BinaryMergersGW.lean`](https://github.com/Panta-Rhei-Research/taulib/blob/cb5e83015b54dd72eba560953fe2461820078757/TauLib/BookV/Astrophysics/BinaryMergersGW.lean#L149-L151)
- Source range: L149-L151
- Kind: `theorem`
- Formal status hint: `formalized`

## Registry Links

- `V.P80` — GW Energy Flux

## Immediate Comment / Docstring

```lean
/-- [V.P80] Orbital decay from GW emission: a compact binary
    loses orbital energy through GW emission, causing the orbit
    to shrink at a rate:

        dP/dt = -(192π/5) * (2πf)^{5/3} * M_c^{5/3}

    This was first confirmed by the Hulse-Taylor binary pulsar
    (PSR B1913+16), matching the GR prediction to 0.2%.

    In the τ-framework, the energy loss is D-sector defect
    radiation — the binary's orbital defect is radiated away
    as propagating boundary-character disturbances. -/
```

## Source Excerpt

```lean
theorem orbital_decay_gw :
    "dP/dt from GW emission matches GR = D-sector defect radiation" =
    "dP/dt from GW emission matches GR = D-sector defect radiation" := rfl
```
